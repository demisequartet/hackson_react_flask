import React from 'react';

    const Answer = ({handleAnswerButtonClick,questions,currentQuestion}) =>{
        return(
            <>
                <h1>音階当てクイズ</h1>
                <h2><span>第{currentQuestion+1}問</span><br></br></h2>
                <ul> 
                {
                    questions[currentQuestion].answerOptions.map((answerOption,key)=>(
                        <li 
                            key={key}
                            onClick={()=>handleAnswerButtonClick(answerOption.isCorrect)}>{answerOption.answerText}
                        </li>)
                    )
                }
                </ul>
            </>
        );
    };

export default Answer;
