using NUnit.Framework;
using PythonExamplesPorterApp;
using System.Diagnostics;
using System.Reflection;
using System.Text;

namespace PythonExamplesPorterAppTests
{
    [TestFixture]
    public class IntegrationTests
    {
        [Test]
        [Ignore("Don't work properly now")]
        public void CheckPortingResultNotWorking()
        {
            const String configPath = "../../../../AWModelLibrary.Examples.PortingResult/config.xml";
            using (StringWriter outputWriter = new StringWriter())
            using (StringWriter errorWriter = new StringWriter())
            {
                String configArg = $"--config={configPath}";
                Int32 returnCode = Program.MainImpl(new[] {configArg}, outputWriter, errorWriter);
                Assert.AreEqual(0, returnCode);
            }
        }

        [Test]
        public void CheckPortingResult()
        {
            const String configPath = "../../../../AWModelLibrary.Examples.PortingResult/config.xml";
            String configArg = $"--config=\"{configPath}\"";
            ExecutionResult result = ExecutionHelper.Execute(new[]{configArg});
            Assert.AreEqual(0, result.ExitCode);
            Assert.IsTrue(String.IsNullOrEmpty(result.Error));
            Console.WriteLine(result.Output);
        }
    }

    internal record ExecutionResult(Int32 ExitCode, String Output, String Error);

    internal static class ExecutionHelper
    {
        public static ExecutionResult Execute(String[] arguments)
        {
            using (Process utilProcess = new Process())
            {
                String currentDir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ?? ".";
                utilProcess.StartInfo.FileName = Path.Combine(currentDir, UtilFilename);
                utilProcess.StartInfo.Arguments = String.Join(" ", arguments);
                utilProcess.StartInfo.UseShellExecute = false;
                utilProcess.StartInfo.CreateNoWindow = true;
                utilProcess.StartInfo.RedirectStandardError = true;
                utilProcess.StartInfo.RedirectStandardOutput = true;
                utilProcess.StartInfo.StandardErrorEncoding = Encoding.UTF8;
                utilProcess.StartInfo.StandardOutputEncoding = Encoding.UTF8;
                utilProcess.StartInfo.WorkingDirectory = currentDir;
                IList<String> output = new List<String>();
                IList<String> error = new List<String>();
                utilProcess.OutputDataReceived += (sender, e) => { output.Add(e.Data ?? ""); };
                utilProcess.ErrorDataReceived += (sender, e) => { error.Add(e.Data ?? ""); };
                utilProcess.Start();
                utilProcess.BeginErrorReadLine();
                utilProcess.BeginOutputReadLine();
                utilProcess.WaitForExit();
                return new ExecutionResult(utilProcess.ExitCode, String.Join("\r\n", output), String.Join("\r\n", error));
            }
        }

        private const String UtilFilename = "PythonExamplesPorterApp.exe";
    }
}
