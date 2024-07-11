/// <reference types="vite/client" />
declare module '*vue' {
    import { ComponentOptions } from "vue";
    const ComponentOptions: ComponentOptions
    export default ComponentOptions
}
declare module 'vue-core-video-player' {
    import { App, Plugin } from 'vue'
  
    const VueCoreVideoPlayerPlugin: Plugin
    export default VueCoreVideoPlayerPlugin
  
    export function install(app: App, ...options: any[]): void
  }

