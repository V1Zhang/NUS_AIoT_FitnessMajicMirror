import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
// import { usePermissStore } from '../store/permiss';
import Home from '../pages/home.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '',
                redirect: '/login',
            },
            {
                path: '/login',
                name: 'Login',
                meta: {
                    title: '登录',
                },
                component: () => import(/* webpackChunkName: "login" */ '../pages/login.vue'),
            },
            // 其他路由
            {
                path: '/mode',
                name: 'Mode',
                meta: {
                    title: '模式选择',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "mode" */ '../pages/mode.vue'),
            },
            {
                path: '/interaction',
                name: 'Interaction',
                meta: {
                    title: '运动交互',
                    permiss: '3',
                },
                component: () => import(/* webpackChunkName: "mode" */ '../pages/interaction.vue'),
            },
        ],
    },
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限',
        },
        component: () => import(/* webpackChunkName: "403" */ '../pages/403.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

// router.beforeEach((to, from, next) => {
//     document.title = `${to.meta.title} | vue-manage-system`;
//     const role = localStorage.getItem('ms_username');
//     const permiss = usePermissStore();
//     if (!role && to.path !== '/login') {
//         next('/login');
//     } else if (to.meta.permiss && !permiss.key.includes(to.meta.permiss)) {
//         // 如果没有权限，则进入403
//         next('/403');
//     } else {
//         next();
//     }
// });

export default router;