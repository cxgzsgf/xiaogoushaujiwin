input_password = self.password_input.text()
        if input_password == self.remote_password:
            self.show_message("成功", "密码验证成功")
            self.enable_functions()
        else:
            self.show_message_and_exit("失败", "密码验证失败")