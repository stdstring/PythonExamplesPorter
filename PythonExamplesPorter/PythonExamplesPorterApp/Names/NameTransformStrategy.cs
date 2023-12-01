using System.Text;

namespace PythonExamplesPorterApp.Names
{
    // Name transformation strategies
    //
    // 1) separatedDigits:
    // Digit groups are separated by underscores from the words preceding and following the group in the name
    // UICompat97To2003=>ui_compat_97_to_2003
    // Rotate90FlipNone => ROTATE_90_FLIP_NONE
    // PlainTable5 => PLAIN_TABLE_5
    // IsoB4 => ISO_B4
    // Standard10x14 => STANDARD_10_X_14
    // AccentColors2to3 => ACCENT_COLORS_2_TO_3
    // Effect3D => EFFECT_3D
    //
    // 2) separatedDigitsExceptSingles (DEFAULT VALUE):
    // Digit groups are separated by underscores from the words preceding and following the digit group in the name, except the following special cases:
    //    * when the name ends with a digit group and does not contain any other digit groups;
    //    * when the digit group precedes the character sequence beginning with the low-case letter, except in cases when the group precedes the character sequence matching the pattern ‘to[next - digit - group]’ (for example ‘97to2003’);
    //    * when the digit group follows the character sequence matching the pattern ‘[previous-digit-group]x’, for example ‘10x15’.
    // UICompat97To2003=>ui_compat_97_to_2003
    // Rotate90FlipNone => ROTATE_90_FLIP_NONE
    // PlainTable5 => PLAIN_TABLE5
    // IsoB4 => ISO_B4
    // Standard10x14=>STANDARD_10X14
    // AccentColors2to3 => ACCENT_COLORS_2_TO_3
    // Effect3D => EFFECT_3D
    //
    // 3) joinedDigits:
    // Digit groups are not separated by underscores from the words preceding and following the group in the name
    // UICompat97To2003=>ui_compat97to2003
    // Rotate90FlipNone => ROTATE90FLIP_NONE
    // PlainTable5 => PLAIN_TABLE5
    // IsoB4 => ISO_B4
    // Standard10x14 => STANDARD10X14
    // AccentColors2to3 => ACCENT_COLORS2TO3
    // Effect3D => EFFECT3D
    //
    // 4) joinedDigitsExceptNumeronyms:
    // Digit groups are not separated by underscores from the words preceding and following the group in the name, except the abbreviations beginning with a digit(such as 2D,3D,5G etc.)
    // UICompat97To2003=>ui_compat97to200
    // Rotate90FlipNone => ROTATE90FLIP_NONE
    // PlainTable5 => PLAIN_TABLE5
    // IsoB4 => ISO_B4
    // Standard10x14=>STANDARD10X14
    // AccentColors2to3 => ACCENT_COLORS2TO3
    // Effect3D => EFFECT_3D
    internal interface INameTransformStrategy
    {
        String ConvertPascalCaseIntoSnakeCase(String name);
    }

    internal class SeparatedDigitsExceptSinglesNameConverter : INameTransformStrategy
    {
        public String ConvertPascalCaseIntoSnakeCase(String name)
        {
            IList<String> parts = new List<String>();
            for (Int32 index = 0; index < name.Length;)
            {
                Char current = name[index];
                switch (current)
                {
                    case '_':
                        parts.Add("_");
                        ++index;
                        break;
                    case var _ when Char.IsLower(current):
                    case var _ when Char.IsUpper(current):
                        String letterPart = CollectLetterPart(name, index);
                        parts.Add(letterPart);
                        index += letterPart.Length;
                        break;
                    case var _ when Char.IsDigit(current):
                        String digitPart = CollectDigitPart(name, index);
                        parts.Add(digitPart);
                        index += digitPart.Length;
                        break;
                }
            }
            return JoinParts(parts);
        }

        private String CollectDigitPart(String source, Int32 start)
        {
            Int32 partSize = 0;
            for (Int32 index = start; index < source.Length; ++index)
            {
                if (!Char.IsDigit(source[index]))
                    break;
                ++partSize;
            }
            return source.Substring(start, partSize);
        }

        private String CollectLetterPart(String source, Int32 start)
        {
            Int32 partSize = 0;
            if ((start + 1 == source.Length) || Char.IsUpper(source[start + 1]))
            {
                for (Int32 index = start; index < source.Length; ++index)
                {
                    if (!Char.IsLetter(source[index]))
                        break;
                    if ((index + 1 < source.Length) && Char.IsLower(source[index + 1]))
                        break;
                    ++partSize;
                }
            }
            else
            {
                partSize = 1;
                for (Int32 index = start + 1; index < source.Length; ++index)
                {
                    if (!Char.IsLower(source[index]))
                        break;
                    ++partSize;
                }
            }
            return source.Substring(start, partSize);
        }

        private String JoinParts(IList<String> parts)
        {
            StringBuilder builder = new StringBuilder();
            JoinState state = new JoinState(parts);
            for (Int32 index = 0; index < parts.Count; ++index)
            {
                state.Index = index;
                switch (parts[index])
                {
                    case "_":
                        builder.Append("_");
                        break;
                    case var part when Char.IsLetter(part[0]):
                        if (NeedUnderscoreForLetterGroup(state))
                            builder.Append("_");
                        builder.Append(part.ToLower());
                        break;
                    case var part when Char.IsDigit(part[0]):
                        if (NeedUnderscoreForDigitGroup(state))
                            builder.Append("_");
                        builder.Append(part);
                        state.HasDigitParts = true;
                        break;
                }
            }
            return builder.ToString();
        }

        private Boolean NeedUnderscoreForLetterGroup(JoinState state)
        {
            Int32 current = state.Index;
            if (current == 0)
                return false;
            if ((current > 0) && (state.Parts[current - 1] == "_"))
                return false;
            if ((current > 0) && (state.Parts[current].Length < 2) && Char.IsDigit(state.Parts[current - 1][0]))
                return false;
            // when the digit group precedes the character sequence beginning with the low-case letter,
            // except in cases when the group precedes the character sequence matching the pattern ‘to[next - digit - group]’ (for example ‘97to2003’)
            if ((current > 0) && Char.IsLower(state.Parts[current][0]) && Char.IsDigit(state.Parts[current - 1][0]))
                return state.Parts[current] == "to";
            return state.Index > 0;
        }
        private Boolean NeedUnderscoreForDigitGroup(JoinState state)
        {
            Int32 current = state.Index;
            if ((current > 0) && (state.Parts[current - 1] == "_"))
                return false;
            // when the name ends with a digit group and does not contain any other digit groups
            if ((current == state.Parts.Count - 1) && !state.HasDigitParts)
                return false;
            // when the digit group follows the character sequence matching the pattern ‘[previous-digit-group]x’, for example ‘10x15’
            if ((current > 1) && (state.Parts[current - 1] == "x") && Char.IsDigit(state.Parts[current - 2][0]))
                return false;
            return true;
        }

        private class JoinState
        {
            public JoinState(IList<String> parts)
            {
                Parts = parts;
                Index = 0;
                HasDigitParts = false;
            }

            public IList<String> Parts { get; }
            public Int32 Index { get; set; }
            public Boolean HasDigitParts { get; set; }
        }
    }

    internal class SimpleFileObjectConverter : INameTransformStrategy
    {
        public String ConvertPascalCaseIntoSnakeCase(String name)
        {
            StringBuilder builder = new StringBuilder();
            for (Int32 index = 0; index < name.Length; ++index)
            {
                Char current = name[index];
                if (Char.IsUpper(current) && (index > 0) && (index < name.Length - 1))
                {
                    Char prev = name[index - 1];
                    Char next = name[index + 1];
                    if (Char.IsLower(prev) ||
                        (Char.IsLower(next) && !Char.IsDigit(prev)) ||
                        (Char.IsDigit(prev) && Char.IsDigit(name[index - 2])))
                        builder.Append('_');
                }
                builder.Append(Char.ToLower(current));
            }

            return builder.ToString();
        }
    }
}
