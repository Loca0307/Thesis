import { combineReducers } from 'redux';
import {
  ADD_TASK,
  EDIT_TASK,
  DELETE_TASK,
  UPDATE_TASK_PROGRESS,
  ADD_CATEGORY,
  EDIT_CATEGORY,
  DELETE_CATEGORY,
} from './actionType';

const initialTasksState = [
  { id: 1, name: 'Task 1', categoryId: 1, completed: false },
  { id: 2, name: 'Task 2', categoryId: 1, completed: true },
];

const initialCategoriesState = [
  { id: 1, name: 'Work' },
  { id: 2, name: 'Personal' },
];

const tasksReducer = (state = initialTasksState, action) => {
  switch (action.type) {
    case ADD_TASK:
      return [...state, action.payload];
    case EDIT_TASK:
      return state.map((task) =>
        task.id === action.payload.id ? { ...task, ...action.payload } : task
      );
    case DELETE_TASK:
      return state.filter((task) => task.id !== action.payload);
    case UPDATE_TASK_PROGRESS:
      return state.map((task) =>
        task.id === action.payload.id ? { ...task, completed: action.payload.completed } : task
      );
    default:
      return state;
  }
};

const categoriesReducer = (state = initialCategoriesState, action) => {
  switch (action.type) {
    case ADD_CATEGORY:
      return [...state, action.payload];
    case EDIT_CATEGORY:
      return state.map((category) =>
        category.id === action.payload.id ? { ...category, ...action.payload } : category
      );
    case DELETE_CATEGORY:
      return state.filter((category) => category.id !== action.payload);
    default:
      return state;
  }
};

export default combineReducers({
  tasks: tasksReducer,
  categories: categoriesReducer,
});