import React from 'react';
import Header from '../../layout/Header/Header';

const Base = ({
    title = "My Title",
    description = "My desription",
    className = "bg-dark text-white p-4",
    children
  }) => {
    return(
        <>
        <Header/>
        <div>{children}</div>
        </>
    )
}

export default Base;