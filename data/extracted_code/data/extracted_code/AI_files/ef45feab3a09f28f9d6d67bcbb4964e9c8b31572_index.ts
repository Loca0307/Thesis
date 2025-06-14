@use '#scss/allPartials' as *;

.#{$px}-favorites-collection-tile {
  display: flex;
  flex-direction: column;
  max-width: 24.5rem;
  text-align: left;

  &__content {
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  &__header {
    align-items: flex-end;
    display: flex;
    justify-content: space-between;
    margin-bottom: $spacing-sm;
  }

  &__info {
    flex: 1;
    overflow: hidden;
  }

  &__count {
    color: $dark-gray;
    display: block;
    margin-bottom: $spacing-xsm;
  }

  h3.#{$px}-text {
    margin-bottom: 0;
  }

  &__title {
    -webkit-box-orient: vertical;
    display: block;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    line-clamp: 1;
    overflow: hidden;

    h3.#{$px}-text {
      margin-bottom: 0;
    }
  }

  &__actions {
    align-items: center;
    align-self: normal;
    background-position: center;
    border-radius: 50%;
    display: flex;
    height: 2.5rem;
    justify-content: center;
    margin-left: $spacing-sm;
    transition: background 0.8s;
    width: 2.5rem;

    &:hover {
      background: $light-gray radial-gradient(circle, transparent 1%, $light-gray 1%) center/15000%;
      background-color: $light-gray;
      cursor: pointer;
    }

    &:active {
      background-color: $medium-gray;
      background-size: 100%;
      transition: background 0s;
    }
  }

  &__popover-content {
    outline: none;
    transform: translateX(2.5rem);
  }

  &__dropdown {
    box-shadow: 0 4px 6px $medium-gray;

    &--item {
      all: unset;
      background-color: $soft-gray;
      cursor: pointer;
      display: block;
      padding: 0.75rem 1rem;
      width: 90px;

      &:hover,
      &:focus-visible {
        background-color: $light-gray;
      }
    }
  }

  &__media-link {
    &:hover {
      color: inherit;
      text-decoration: none;
    }
  }

  &__media-container {
    position: relative;
    width: 100%;
  }

  &__media {
    background-position: center;
    width: 100%;
  }

  &__empty {
    aspect-ratio: 1 / 1;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    cursor: pointer;
    display: block;
    position: relative;

    &--favorites {
      background-color: $soft-gray;
    }

    &--list {
      border: 1px solid #0000001f;
      border-radius: 0;
    }

    &__content {
      bottom: 20px;
      left: 20px;
      position: absolute;
    }
  }

  &__icon {
    grid-column: 1;
    justify-self: start;

    &-rotate {
      transform: rotate(90deg);
    }
  }

  &__text {
    color: $dark-gray;
    font-size: $body-size3;
    font-variation-settings: 'wght' 400;
    padding-top: 5px;
  }

  [data-radix-popper-content-wrapper] > * {
    all: unset;
  }
}