# DX_pass

## 简介
一个基于前端生成 DX Pass 的应用，用户可以通过简单的界面生成 DX Pass  
可以通过修改 HTML 文件中的路径配置将项目部署到 Cloudflare Pages 等平台，实现快速搭建和在线使用  
感谢 妖梦bot 提供的参考

---

## 安装

### 环境要求
- Python 3.8 或更高版本

### 安装步骤
1. 拉取项目所有文件：
   ```bash
   git clone https://github.com/ZzzZJHha/DX_pass.git
   cd DX_pass
   ```
2. 安装依赖：
   ```bash
   pip install gevent flask
   ```
## 运行
运行以下命令启动项目：
   ```bash
   python app.py
   ```
默认服务器运行在 http://127.0.0.1:2233

---

## 开源协议
本项目采用 [Affero General Public License (AGPL)](https://www.gnu.org/licenses/agpl-3.0.html) 开源
