import React from 'react';

const SortFilter = ({ sortOption, onSortChange }) => {
  return (
    <select value={sortOption} onChange={(e) => onSortChange(e.target.value)}>
      <option value="newest">Newest</option>
      <option value="highest">Highest Rated</option>
      <option value="lowest">Lowest Rated</option>
      <option value="rising">Rising</option>
      <option value="controversial">Most Controversial</option>
      <option value="random">Random</option>
    </select>
  );
};

export default SortFilter;