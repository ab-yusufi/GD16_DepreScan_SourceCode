import React from 'react';
import './PrimaryButton.css'

const PrimaryButton = ({title, onClick}) => {
    return(
        <button className="btn" onClick={() => onClick()}>
            {title}
        </button>
    )
}

export default PrimaryButton;