<template>
  <q-layout view="lHh Lpr lFf">
    <!-- <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          SPM App
        </q-toolbar-title>

        
      </q-toolbar>
    </q-header> -->

    <q-header class="q-px-sm " style="background-color:white;;color:black" v-if="!$route.fullPath.includes('login')" >
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          color="white"
          @click="leftDrawerOpen = !leftDrawerOpen"
        /> -->

        <img src="~assets/LJPS_logo.svg" alt="">

        
        
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      v-if="!$route.fullPath.includes('login')"
      :width="250"
      
      :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
      
    >
      <q-list class="" style="background-color:#f2f2f2;height:100%">
        <q-item
        clickable
        tag="a"
        :to="'/learning_journey/'+this.$store.state.user"
      >
        <q-item-section
          avatar
        >
          <q-icon name="auto_stories" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Learning Journeys</q-item-label>
          
        </q-item-section>
      </q-item>

      <q-item
        clickable
        tag="a"
        :to="'/Jobs'"
      >
        <q-item-section
          avatar
        >
          <q-icon name="work" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Job Roles</q-item-label>
          
        </q-item-section>
      </q-item>

      <q-item
        clickable
        tag="a"
        :to="'/HR'"
        v-if="this.$store.state.user == 'hr'"
      >
        <q-item-section
          avatar
        >
          <q-icon name="person" />
        </q-item-section>

        <q-item-section>
          <q-item-label>HR Management</q-item-label>
          
        </q-item-section>
      </q-item>

      <q-item
        clickable
        tag="a"
        @click="logout()"
       
      >
        <q-item-section
          avatar
        >
          <q-icon name="logout" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Logout</q-item-label>
          
        </q-item-section>
      </q-item>


<!-- 
        <q-item
        v-for="link in essentialLinks"
        :key="link.title"
        v-bind="link"
        clickable
        tag="a"
        :to="link.link"
       
        
      >
        <q-item-section
          v-if="link.icon"
          avatar
        >
          <q-icon :name="link.icon" />
        </q-item-section>

        <q-item-section>
          <q-item-label>{{ link.title }}</q-item-label>
          
        </q-item-section>
      </q-item>
        -->
       
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [

  {
    title: 'Learning Journeys',
    icon: 'auto_stories',
    link: '/learning_journey'
  },
  {
    title: 'Job Roles',
  
    icon: 'work',
    link: '/Jobs'
  },
  {
    title: 'HR Management',
    icon: 'person',
    link: '/HR',
  },
  {
    title: 'Logout',
    icon: 'logout',
    link: '/login'
  },
  
]

export default {
  methods: {
    logout(){
      localStorage.setItem("token", '')
      this.$router.push('/login')
    }
  },
  name: 'MainLayout',
  components: {
    EssentialLink
  },
  data () {
    return {
      miniState:true,
      leftDrawerOpen: false,
      
      essentialLinks: linksData
    }
  },
  mounted(){
    if (localStorage.token == undefined){
      this.$router.push('/login')
    } 

    if (this.$store.state.user == ''){
      this.$router.push('/login')
    }
  
  }
}
</script>
