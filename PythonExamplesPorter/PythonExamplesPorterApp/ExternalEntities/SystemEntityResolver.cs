using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.Expressions;
using PythonExamplesPorterApp.ExternalEntities.SystemResolvers;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class SystemEntityResolver : IExternalEntityResolver
    {
        public SystemEntityResolver(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _resolvers = GetSystemMemberResolvers(model, appData, settings);
        }

        public OperationResult<MemberResolveData> ResolveCtor(ITypeSymbol sourceType, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            ISystemMemberResolver? resolver = _resolvers.FirstOrDefault(source => source.TypeName == sourceTypeFullName);
            if (resolver == null)
                return new OperationResult<MemberResolveData>.Error($"Unsupported type: {sourceTypeFullName}");
            return resolver.ResolveCtor(argumentsData, argumentsRepresentation);
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            ISystemMemberResolver? resolver = _resolvers.FirstOrDefault(source => source.TypeName == sourceTypeFullName);
            if (resolver == null)
                return new OperationResult<MemberResolveData>.Error($"Unsupported type: {sourceTypeFullName}");
            return resolver.ResolveMember(data, representation);
        }

        public OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation)
        {
            return new OperationResult<CastResolveData>.Error("Not supported now");
        }

        private IList<ISystemMemberResolver> GetSystemMemberResolvers(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            return new List<ISystemMemberResolver>
            {
                new SystemStringMemberResolver(model),
                new SystemConsoleMemberResolver(model, appData, settings),
                new SystemDrawingColorMemberResolver(model, appData),
                new SystemDrawingPointMemberResolver(model, appData, "Point"),
                new SystemDrawingPointMemberResolver(model, appData, "PointF"),
                new SystemDrawingSizeMemberResolver(model, appData, "Size"),
                new SystemDrawingSizeMemberResolver(model, appData, "SizeF"),
                new SystemDrawingRectangleMemberResolver(model, appData, "Rectangle"),
                new SystemDrawingRectangleMemberResolver(model, appData, "RectangleF"),
                new SystemDateTimeMemberResolver(model),
                new SystemGuidMemberResolver(model),
                new SystemTimeSpanMemberResolver(model),
                new SystemIoSearchOptionMemberResolver(model),
                new SystemIoFileMemberResolver(model),
                new SystemIoFileInfoMemberResolver(model),
                new SystemIoDirectoryMemberResolver(model),
                new SystemSpecialFolderMemberResolver(model),
                new SystemEnvironmentMemberResolver(model),
                new SystemIoPathMemberResolver(model),
                new SystemIListMemberResolver(model),
            };
        }

        private readonly IList<ISystemMemberResolver> _resolvers;
    }
}