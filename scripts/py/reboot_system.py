        if self.check_fastboot_connection():
            self.show_message("提示", "即将重启系统")
            self.execute_command([self.fastboot_path, "reboot"])