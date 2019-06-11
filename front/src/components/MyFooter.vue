<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  .my-footer{
    // height: 226px;
    margin-top: 30px;
    border-top: 1px solid #e0dfdf;
    background-color: black;
    padding: 15px;
    text-align: center;
    & > div{
      color: #fff;
      text-align: center;
      & > div{
        display: inline-block;
        min-width: 370px;
        & > div{
          margin-bottom: 15px;
          text-align: left;
        }
      }
      span, a {
        color: #fff;
      }
    }
  }
  .row{
    margin: 0;
  }
</style>
<template>
  <div class="my-footer row">
    <div class="col-md-7">
      <div>
        <div>
          网站作者：
          <span>张云</span>
        </div>
        <div>
          院校：
          <span>贵州大学 软件工程学院</span>
        </div>
        <div>
          邮箱：
          <span>3181114965@qq.com</span>
        </div>
      </div>
    </div>
    <div class="col-md-5">
      <div>
        <div>
          网站主要技术点：<br>
          <span>Vue, bootstrap, less, python, flask, uwsgi, nginx, mysql</span>
        </div>
      </div>
    </div>
  </div>
</template>
