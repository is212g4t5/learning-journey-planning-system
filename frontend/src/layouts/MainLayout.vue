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

    <q-header class="q-px-sm " style="background-color:white;;color:black" >
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
      
      :width="250"
      
      :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
      
    >
      <q-list class="" style="background-color:#f2f2f2;height:100%">

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
       
        <!-- <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        /> -->
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
    title: 'Home',
    caption: 'quasar.dev',
    icon: 'dashboard',
    link: '/home'
  },
  {
    title: 'Courses',
    caption: 'github.com/quasarframework',
    icon: 'auto_stories',
    link: '/Courses'
  },
  {
    title: 'Job Roles',
    caption: 'github.com/quasarframework',
    icon: 'work',
    link: '/Jobs'
  },
  {
    title: 'HR Management',
    caption: 'github.com/quasarframework',
    icon: 'person',
    link: '/HR'
  },
  {
    title: 'Logout',
    caption: 'forum.quasar.dev',
    icon: 'logout',
    link: ''
  },
  
]

export default {
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

  this.$router.push('/home')
  }
}
</script>
