import axios from 'axios';

// Inintial
const state = {
  mhs: null,
  mh: null
};

// Retrive values of all mental health entry and single entry

const getters = {
  stateMhs: state => state.mhs,
  stateMh: state => state.mh,
};

// API call
const actions = {
  async createMh({dispatch}, mh) {
    await axios.post('mh', mh);
    await dispatch('getmhs');
  },
  async getMhs({commit}) {
    let {data} = await axios.get('mh');
    commit('setMhs', data);
  },
  async viewmh({commit}, id) {
    let {data} = await axios.get(`mh/${id}`);
    commit('setMh', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateMh({}, mh) {
    await axios.patch(`mh/${mh.id}`, mh.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteMh({}, id) {
    await axios.delete(`mh/${id}`);
  }
};

const mutations = {
  setMhs(state, mhs){
    state.mhs = mhs;
  },
  setMh(state, mh){
    state.mh = mh;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};