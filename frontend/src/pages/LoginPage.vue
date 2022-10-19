<template>
  <q-page class="">
   
    <div class="q-px-xl flex no-wrap items-center justify-around" style="background:#FFF3E4" >
      <div class="">
        <div class="" style="font-size:50px;font-weight:600;line-height:60px">Turn your ambition <br>into a success story</div>
        <div class="q-mt-md" style="width:500px;font-size:18px;font-weight:300">With LJPS, planning your own learning journey and achieving your desired job role has never been easier!</div>
      </div>
      
      <img src="~assets/header-bg.png" alt="" style="width:400px;">
    </div>

    <div
      class="text-center font-700 q-mt-md"
      style="color: #525252; font-size: 28px; "
    >
      Login As...
    </div>
    <div
      class="q-mx-auto q-mb-lg"
      style="background-color: #a8a8ff; width: 75px; height: 2px"
    ></div>

    <div class="flex justify-around items-center q-mx-auto " style="width:75%">
      <!-- HR card div -->
      <div class="q-pa-lg loginCard purpleLoginCard" style="background:#e0e0e9;width:300px; border-radius:15px" @click="login('Human Resource')">
        <div class="flex justify-center items-center" style="background:#a6a6f2;width:75px;height:75px; border-radius: 10px;">
          <q-icon name="engineering" style="font-size:50px"></q-icon>
        </div>

        <div class="q-mt-md" style="font-size:28px; font-weight:500">Human Resource</div>
        <div
          class="q-mb-lg"
          style="background-color: #a8a8ff; width: 75px; height: 4px"
        ></div>

        <div class="flex justify-center">
           <q-btn label="Login" no-caps style="background:#a6a6f2;color:white; margin-top:50px;width:75%" size="lg" ></q-btn>
        </div>
      </div>

      <!-- Other user card div -->
      <div class="q-pa-lg loginCard yellowLoginCard" style="background:#fbecd7 ;width:300px; border-radius:15px" @click="login('Other User')">
        <div class="flex justify-center items-center" style="background:#f5cb96;width:75px;height:75px; border-radius: 10px;">
          <q-icon name="groups" style="font-size:50px"></q-icon>
        </div>

        <div class="q-mt-md" style="font-size:28px; font-weight:500">Other User</div>
        <div
          class="q-mb-lg"
          style="background-color: #ecad6e; width: 75px; height: 4px"
        ></div>

        <div class="flex justify-center">
           <q-btn label="Login" no-caps style="background:#f5cb96;color:white; margin-top:50px;width:75%" size="lg" ></q-btn>
        </div>
      </div>

      <!-- Manager card div -->
      <div class="q-pa-lg loginCard blueLoginCard" style="background:#dcf7fe ;width:300px; border-radius:15px" @click="login('Manager')">
        <div class="flex justify-center items-center" style="background:#bae6f1;width:75px;height:75px;border-radius: 10px;">
          <q-icon name="person" style="font-size:50px"></q-icon>
        </div>

        <div class="q-mt-md" style="font-size:28px; font-weight:500">Manager</div>
        <div
          class="q-mb-lg"
          style="background-color: #83c4d4; width: 75px; height: 4px"
        ></div>

        <div class="flex justify-center">
           <q-btn label="Login" no-caps style="background:#8cdaec;color:white; margin-top:50px;width:75%" size="lg" ></q-btn>
        </div>
      </div>





    </div>
    
    <q-dialog v-model="loginDialog">
      <q-card style="width:50vw;border-radius:15px" class="q-pa-md">
        <q-card-section>
          <div class="text-h4 text-center">{{user}}</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
         <div class="" style="font-size:18px">Staff email</div>
         <q-input v-model="email" outlined placeholder="Enter Staff Email" />


        </q-card-section>

        <q-card-actions >
          <div class="q-mx-auto q-gutter-x-md">
            <q-btn label="Login" v-close-popup no-caps size="md" style="width:10vw;background:#afdfa5 " @click="handleRedirect()" />
            <q-btn label="Cancel" v-close-popup no-caps size="md" style="width:10vw;background:#e4e4e4" />
          </div>
          
        </q-card-actions>
      </q-card>
    </q-dialog>

    


  </q-page>
</template>

<script>
export default {
  methods: {
    login(user){
      this.loginDialog = true
      this.user = user
    },
    handleRedirect(){
      //add juan api after this


      if (this.user == 'Human Resource'){

        localStorage.setItem("token", 'hr')

        this.$store.state.user = 'hr'
        this.$router.push('/learning_journey/hr')
      }else if (this.user == 'Manager'){
        localStorage.setItem("token", 'manager')
        this.$store.state.user = 'manager'
        this.$router.push('/learning_journey/manager')
      }else if (this.user == 'Other User'){
        localStorage.setItem("token", 'user')
        this.$store.state.user = 'user'
        this.$router.push('/learning_journey/user')
      }
    }
  },
  mounted(){
    // if (this.user == 'Human Resource'){
    //   this.$store.state.user = 'hr'
    // }else if (this.user == 'Manager'){
    //   this.$store.state.user = 'manager'
    // }else if (this.user == 'Other User'){
    //   this.$store.state.user = 'user'
    // }



    
  },  
  data () {
    return {
      loginDialog:false,
      user:'',
      email:'',
      password:''
    }
  },
  
}
</script>

<style scoped>

.loginCard{
  transition: 0.2s;
  cursor:pointer;
}

.yellowLoginCard:hover{
  transform:translateY(-10px);
  box-shadow: rgb(254 153 2) 0px 0px 20px;
}


.purpleLoginCard:hover{
  transform:translateY(-10px);
  box-shadow: rgb(100, 100, 226) 0px 0px 20px;
}
.blueLoginCard:hover{
  transform:translateY(-10px);
  box-shadow: rgb(86, 200, 225) 0px 0px 20px;
}


</style>
