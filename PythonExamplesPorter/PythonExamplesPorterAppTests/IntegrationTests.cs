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
            using (StringWriter outputWriter = new StringWriter())
            using (StringWriter errorWriter = new StringWriter())
            {
                String configArg = $"--config={ConfigPath}";
                Int32 returnCode = Program.MainImpl(new[] {configArg}, outputWriter, errorWriter);
                Assert.AreEqual(0, returnCode);
            }
        }

        [Test]
        public void CheckPortingResult()
        {
            String configArg = $"--config=\"{ConfigPath}\"";
            ExecutionResult result = ExecutionHelper.Execute(new[]{configArg});
            Assert.AreEqual(0, result.ExitCode);
            Assert.IsTrue(String.IsNullOrEmpty(result.Error));
            Console.WriteLine(result.Output);
        }

        [Test]
        public void GetPorterVersion()
        {
            String versionArg = "--version";
            ExecutionResult result = ExecutionHelper.Execute(new[] {versionArg});
            CheckResult(result, 0, "C# to Python example porter\r\n0.0.1\r\n", "");
        }

        [Test]
        public void GetPorterHelp()
        {
            String helpArg = "--help";
            ExecutionResult result = ExecutionHelper.Execute(new[] {helpArg});
            CheckResult(result, 0, "C# to Python example porter\r\nUsage: <app> --config=<path to config file>\r\n", "");
        }

        [Test]
        public void ProcessWrongArgs()
        {
            String someArg = "--some-arg";
            ExecutionResult result = ExecutionHelper.Execute(new[] {someArg});
            CheckResult(result, 666, "C# to Python example porter\r\nUsage: <app> --config=<path to config file>\r\n", "Wrong config data");
        }

        [Test]
        public void ProcessWrongConfig()
        {
            String configArg = "--config=\"./SomeUnknownConfig.cfg\"";
            ExecutionResult result = ExecutionHelper.Execute(new[]{configArg});
            CheckResult(result, 999, "C# to Python example porter\r\n", "Unhandled exception:\r\nSystem.IO.FileNotFoundException:");
        }

        private void CheckResult(ExecutionResult result, Int32 exitCode, String output, String error)
        {
            Assert.AreEqual(exitCode, result.ExitCode);
            Assert.AreEqual(output, result.Output);
            Assert.IsTrue(result.Error.StartsWith(error));
        }

        const String ConfigPath = "../../../../AWModelLibrary.Examples.PortingResult/config.xml";
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
