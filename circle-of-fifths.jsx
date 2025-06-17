import { useState } from 'react';

const circleData = [
  { key: 'C', chords: ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'] },
  { key: 'G', chords: ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'] },
  { key: 'D', chords: ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'] },
  { key: 'A', chords: ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'] },
  { key: 'E', chords: ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'] },
  { key: 'B', chords: ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'] },
  { key: 'F#', chords: ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim'] },
  { key: 'Gb', chords: ['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm', 'Fdim'] },
  { key: 'Db', chords: ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'] },
  { key: 'Ab', chords: ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim'] },
  { key: 'Eb', chords: ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'] },
  { key: 'Bb', chords: ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'] },
  { key: 'F', chords: ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'] }
];

export default function CircleOfFifths() {
  const [selectedKey, setSelectedKey] = useState(null);

  const handleClick = (key) => {
    setSelectedKey(key);
  };

  return (
    <div className="flex flex-col items-center p-6">
      <h1 className="text-2xl font-bold mb-4">Circle of Fifths</h1>
      <div className="grid grid-cols-4 gap-4 mb-6">
        {circleData.map((entry) => (
          <button
            key={entry.key}
            className={`rounded-full w-16 h-16 flex items-center justify-center border text-lg font-bold transition-colors duration-200 ${
              selectedKey === entry.key ? 'bg-black text-white' : 'bg-white text-black border-gray-400'
            }`}
            onClick={() => handleClick(entry.key)}
          >
            {entry.key}
          </button>
        ))}
      </div>
      {selectedKey && (
        <div className="text-center">
          <h2 className="text-xl font-semibold mb-2">Chords in {selectedKey} Major</h2>
          <div className="flex flex-wrap justify-center gap-2">
            {circleData.find((entry) => entry.key === selectedKey)?.chords.map((chord) => (
              <span
                key={chord}
                className="px-4 py-2 bg-green-200 rounded shadow text-lg"
              >
                {chord}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
