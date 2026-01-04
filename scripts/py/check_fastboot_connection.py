     def check_fastboot_connection(self):
   command = [self.fastboot_path, "devices"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stdout.strip():
            self.show_message("成功", "Fastboot 连接正常")
            return True
        else:
            self.show_message("失败", "没有检测到 fastboot 设备")
            return False