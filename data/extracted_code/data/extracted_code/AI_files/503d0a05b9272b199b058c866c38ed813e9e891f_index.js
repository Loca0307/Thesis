import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      count: 0
    };
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  },
  actions: {
    incrementAction({ commit }) {
      commit('increment');
    }
  },
  getters: {
    doubleCount: (state) => state.count * 2
  }
});

export default store;