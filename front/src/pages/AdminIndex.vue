<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme.less';
  header {
    text-align: center;
    padding: 20px;
    border-bottom: 1px solid #e0dfdf;
    background-color: #fff;
    font-size: 16px;
    font-weight: 700;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  #admin-login{
    min-height: 100vh;
  }

</style>
<template>
  <div id="admin-login">
    <header>
      管理系统
    </header>
    <el-row>
      <el-col :span="4">
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="1" @click="changeTab('userManage')">
            <i class="el-icon-menu"></i>
            <span slot="title" >用户管理</span>
          </el-menu-item>
          <el-menu-item index="2" @click="changeTab('proManage')">
            <i class="el-icon-setting"></i>
            <span slot="title">项目管理</span>
          </el-menu-item>
          <el-menu-item index="3" @click="changeTab('appealManage')">
            <i class="el-icon-setting"></i>
            <span slot="title" >申诉系统</span>
          </el-menu-item>
          <!-- <el-menu-item index="4" @click="changeTab('advManage')">
            <i class="el-icon-setting"></i>
            <span slot="title" >广告管理</span>
          </el-menu-item> -->
        </el-menu>
      </el-col>
      <el-col :span="20">
        <component :is="currentTab"></component>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import UserManage from '@/components/UserManage'
  import AppealManage from '@/components/AppealManage'
  import AdvManage from '@/components/AdvManage'
  import ProManage from '@/components/ProManage'


  export default {
    data () {
      return {
        currentTab: 'userManage'
      }
    },
    methods: {
      changeTab (tab) {
        this.currentTab = tab
      }
    },
    components: {
      UserManage,
      AppealManage,
      AdvManage,
      ProManage
    }
  }
</script>
