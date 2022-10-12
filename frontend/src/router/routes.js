
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'login', component: () => import('src/pages/LoginPage.vue') },
      { path: 'HR', component: () => import('pages/HRManagement_Page.vue') },
      { path: 'learning_journey', component: () => import('src/pages/LearningJourneyPage.vue') },
      { path: 'Jobs', component: () => import('pages/JobsPage.vue') },
      { path: 'JobDetails/:id', component: () => import('pages/JobDetailsPage.vue') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
