import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import mh from './modules/mh';
import users from './modules/users';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    mh,
    users,
  },
  plugins: [createPersistedState()]
});