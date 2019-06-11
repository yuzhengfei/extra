<style lang="less" rel="stylesheet/less" scoped>
  @import '../css/theme';
  .talk-page{
    padding-top: 60px;
    & > div{
      background-color: #fff;
      width:90%;
      padding: 10px 15px;
      margin: 0 auto;
      margin-top: 60px;
      border-radius: 4px;
      & > header{
        padding-bottom: 20px;
        border-bottom: 1px solid #ccc;
        font-weight: 600;
        box-sizing: border-box;
        span{
          padding: 15px 8px;
          cursor: pointer;
        }
      }
      .talk-container{
        padding: 30px 0;
        box-sizing: border-box;
      }
    }
  }
  .clicked{
    border-bottom: 2px solid @secondColor;
  }
  .projects-container-tip{
    text-align: center;
    color: @secondColor;
  }
</style>
<template>
  <div class="talk-page">
    <div>
        <el-button type="success" @click="dialogFormVisible = true">发布帖子</el-button>
        <el-dialog title="帖子" :visible.sync="dialogFormVisible">
            <el-form :model="form" :rules="rules" ref="form" >
                <el-form-item label="标题" :label-width="formLabelWidth" prop="name" >
                <el-input v-model="form.name" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitForm('form')">确 定</el-button>
            </div>
       </el-dialog>
        <el-table
    :data="tableData"
    style="width: 100%">
    <!-- <el-table-column
      label="帖子"
      width="600">
      <template slot-scope="scope">
        <i class="el-icon-document-copy"></i>
        <span style="margin-left: 10px">{{ scope }}</span>
      </template>
    </el-table-column> -->
     <el-table-column
        prop="content"
        label="标题"
        width="400">
      </el-table-column> 
      <el-table-column
        prop="createTime"
        label="时间"
        width="280">
      </el-table-column> 
       <el-table-column
        prop="userName"
        label="发布人"
        width="280">
      </el-table-column> 
       
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">回复</el-button>
      </template>
    </el-table-column>
  </el-table>
    </div>
  </div>
</template>
<script>
  import {baseUrl} from '@/config/config'
  export default {
    data () {
      return {
        baseUrl:baseUrl,
        dialogFormVisible: false,
        form: {
          name: ''
        },
        tableData: [],
        formLabelWidth: '120px',
        rules: {
          name: [
            { required: true, message: '请输入帖子标题', trigger: 'blur' }
          ]
        }
      }
  },
    mounted () {

    },
    beforeRouteEnter (to, from, next) {
      next(vm => {
        // if (!vm.$store.state.hasLogin) {
        //   alert('请先登录')
        //   vm.$router.push({name: 'index'})
        // }
        vm.$store.commit('changeSingerState', {stateName: 'myHeader', value: true})
      })
    },
    created(){
      this.getpost()
    },




    methods: {
      handleEdit (index, row) {
        console.log(row.id)
        // this.$router.push({path:'xxx',params:{id:'123'})
       this.$router.push({path: 'PostReply', query: {id: row.id}})
      },
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.subimtsave()
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      // 获取帖子列表
      getpost () {
        this.$http.get(baseUrl + 'questionList', {})
          .then(res => {
            if (res.status === 200) {
              this.tableData = res.data
              console.log(this.tableData)
            }
          }, res => {
            alert('发布失败，请检查网络')
          })
      },
      subimtsave () {
        let store = window.localStorage
        let userId = store['token'].split('-')[0]
        this.$http.post(baseUrl + 'questionSave', {
          userId: userId,
          content: this.form.name
        })
          .then(res => {
             if(res.data ==='1'){
               this.dialogFormVisible = false;
                  // this.$message({
                  //   message: '恭喜你，发帖成功',
                  //   type: 'success'
                  // });
                  this.form.name = "";
                  this.getpost()
             }
          }, res => {
            alert('发布失败，请检查网络')
          })
      }
    },
    components: {

    }
  }
</script>

