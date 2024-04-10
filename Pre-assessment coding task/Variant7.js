import React, { useState } from 'react';

const MultiplicationTable = () => {
  const size = 12;
  const [highlightedNumber, setHighlightedNumber] = useState(null);

  // セルをクリックしたときのハンドラー
  const handleCellClick = (number) => {
    setHighlightedNumber(number);
  };

  // テーブルのセルを生成する関数
  const renderCell = (i, j) => {
    const number = i * j;
    const isHighlighted = number === highlightedNumber;
    const cellClass = isHighlighted ? 'highlight' : '';
    const CellTag = i === 1 || j === 1 ? 'th' : 'td';

    return (
      <CellTag
        key={`${i}-${j}`}
        className={cellClass}
        onClick={() => handleCellClick(number)}
      >
        {number}
      </CellTag>
    );
  };

  // 掛け算表を生成する関数
  const renderTable = () => {
    const rows = [];
    for (let i = 1; i <= size; i++) {
      const cells = [];
      for (let j = 1; j <= size; j++) {
        cells.push(renderCell(i, j));
      }
      rows.push(<tr key={i}>{cells}</tr>);
    }
    return <table>{rows}</table>;
  };

  return (
    <div>
      <h1>12x12の掛け算表</h1>
      {renderTable()}
    </div>
  );
};

export default MultiplicationTable;

//i'm not sure