// __tests__/textUtils.test.ts
import { findCprNumbers } from '@/textUtils';

describe('findCprNumbers', () => {
  it('should find valid CPR numbers with hyphens', () => {
    const text = 'Valid CPR: 010203-1234 and 040506-5678.';
    const result = findCprNumbers(text);
    expect(result).toEqual(['010203-1234', '040506-5678']);
  });

  it('should find valid CPR numbers without hyphens', () => {
    const text = 'Valid CPR: 0102031234 and 0405065678.';
    const result = findCprNumbers(text);
    expect(result).toEqual(['0102031234', '0405065678']);
  });

  it('should not find invalid CPR numbers', () => {
    const text = 'Invalid CPR: 320199-1234 and 31 02 31 1234.';
    const result = findCprNumbers(text);
    expect(result).toEqual([]);
  });

  it('should return an empty array if no CPR numbers are found', () => {
    const text = 'No CPR numbers here.';
    const result = findCprNumbers(text);
    expect(result).toEqual([]);
  });

  it('should handle an empty string gracefully', () => {
    const text = '';
    const result = findCprNumbers(text);
    expect(result).toEqual([]);
  });
});