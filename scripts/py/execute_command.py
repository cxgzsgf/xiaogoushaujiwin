  try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print(result.stdout)
            return True
        except subprocess.CalledProcessError as e:
            print("执行命令时出错:", e.stderr)
            self.show_message("错误", e.stderr)
            return False