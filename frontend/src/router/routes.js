
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'home', component: () => import('pages/Index.vue') },
      { path: 'HR', component: () => import('pages/HRManagement_Page.vue') },
      { path: 'Courses', component: () => import('pages/CoursesPage.vue') },
      { path: 'Jobs', component: () => import('pages/JobsPage.vue') },
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
