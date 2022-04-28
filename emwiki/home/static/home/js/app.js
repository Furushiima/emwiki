import {News} from './components/News.js';

new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  components: {
    'news': News,
  },
  data: () => ({
    drawerExists: false,
    drawerWidth: 256,
    disableResizeWatcher: true,
    menuButton: false,
  }),
  delimiters: ['$(', ')'],
});
