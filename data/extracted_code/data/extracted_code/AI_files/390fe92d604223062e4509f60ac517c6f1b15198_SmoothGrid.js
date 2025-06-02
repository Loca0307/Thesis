/** Creates A Div Element With A ease-in-out Transition Of
 * grid-template-columns
 * grid-template-rows
 * gap
 * on an automatic div element with grid mutations
*/

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Transition } from 'react-transition-group';

export default class SmoothGrid extends Component { // eslint-disable-line react/prefer-stateless-function
  static propTypes = {
    children: PropTypes.node,
    style: PropTypes.object,
    className: PropTypes.string,
    gridTemplateColumns: PropTypes.string,
    gridTemplateRows: PropTypes.string,
    gap: PropTypes.string,
    duration: PropTypes.number,
    onEnter: PropTypes.func,
    onEntered: PropTypes.func,
    onEntering: PropTypes.func,
    onExit: PropTypes.func,
    onExited: PropTypes.func,
    onExiting: PropTypes.func,
  };

  static defaultProps = {
    duration: 300,
  };

  render() {
    const {
      children,
      style,
      className,
      gridTemplateColumns,
      gridTemplateRows,
      gap,
      duration,
      onEnter,
      onEntered,
      onEntering,
      onExit,
      onExited,
      onExiting,
      ...props
    } = this.props;

    return (
      <Transition
        {...props}
        timeout={{
          enter: duration,
          exit: duration,
        }}
        onEnter={onEnter}
        onEntered={onEntered}
        onEntering={onEntering}
        onExit={onExit}
        onExited={onExited}
        onExiting={onExiting}
      >
        {state => (
          <div
            style={{
              ...style,
              gridTemplateColumns,
              gridTemplateRows,
              gap,
              transition: `all ${duration}ms ease-in-out`,
              ...(state === 'entered' && {
                gridTemplateColumns: 'auto',
                gridTemplateRows: 'auto',
                gap: '0',
              }),
            }}
            className={`smooth-grid ${className}`}
          >
            {children}
          </div>
        )}
        </Transition>
    );
  }
}