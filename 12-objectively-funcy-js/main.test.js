const {
  getFirstName,
  getLastName,
  getFullName,
  setFirstName,
  setAge,
  giveBirthday,
  marry,
  divorce,
} = require('./main.js')


describe('getFirstName', () => {
  it(`returns the first name of the given person`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Redacted Jaffe'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    expect(getFirstName(person1)).toBe('Colin')
    expect(getFirstName(person2)).toBe('Petra')
  })
});

describe('getLastName', () => {
  it(`returns the last name of the given person`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Redacted Jaffe'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    expect(getLastName(person1)).toBe('Jaffe')
    expect(getLastName(person2)).toBe('Solano')
  })
});

describe('getFullName', () => {
  it(`returns the first name and last name of the given person, with a space in the middle`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Redacted Jaffe'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    expect(getFullName(person1)).toBe('Colin Jaffe')
    expect(getFullName(person2)).toBe('Petra Solano')
  })
})

describe('setFirstName', () => {
  it('gives the given name to the person object as its firstName property', () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Redacted Jaffe'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    setFirstName(person1, 'Redacted');
    expect(person1.firstName).toBe('Redacted');
    setFirstName(person2, 'Anthony');
    expect(person2.firstName).toBe('Anthony');
  })
})

describe(`setAge`, () => {
  it(`sets age on the given person`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Redacted Jaffe'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    setAge(person1, 45);
    expect(person1.age).toBe(45)
    setAge(person2, 35);
    expect(person2.age).toBe(35)
  })
})

describe('giveBirthday', () => {
  it(`ages the given person up by 1`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Redacted Jaffe'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    giveBirthday(person1);
    giveBirthday(person1);

    giveBirthday(person2);
    giveBirthday(person2);
    giveBirthday(person2);

    expect(person1.age).toBe(41);
    expect(person2.age).toBe(32);
  })

  it(`gives the person an age of 1 if they didn't previously have an age`, () => {
    const baby = {
      firstName: 'Redacted Jr.',
      lastName: 'Jaffe',
    };

    giveBirthday(baby);
    expect(baby.age).toBe(1);
  })
})

describe('marry', () => {
  it(`sets the marital status of both given people to true`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: false,
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    marry(person1, person2);
    expect(person1.married).toBe(true);
    expect(person2.married).toBe(true);
  })

  it(`sets the spouse of each given person to be the full name of the other`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: false,
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: false,
    };

    const person3 = {
      firstName: 'Michael',
      lastName: 'Cordero',
      age: 33,
      married: false,
    };

    const person4 = {
      firstName: 'Jane',
      lastName: 'Villanueva',
      age: 28,
      married: false,
    };

    marry(person1, person2);
    expect(person1.spouseName).toBe('Petra Solano');
    expect(person2.spouseName).toBe('Colin Jaffe');

    marry(person3, person4);
    expect(person3.spouseName).toBe('Jane Villanueva')
    expect(person4.spouseName).toBe('Michael Cordero')
  })
})

describe('divorce', () => {
  it(`sets the marital status of both people to false`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Petra Solano'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: true,
      spouseName: 'Colin Jaffe'
    };

    const person3 = {
      firstName: 'Michael',
      lastName: 'Cordero',
      age: 33,
      married: true,
      spouseName: 'Jane Villanueva',
    };

    const person4 = {
      firstName: 'Jane',
      lastName: 'Villanueva',
      age: 28,
      married: true,
      spouseName: 'Michael Cordero'
    };

    divorce(person1, person2);
    expect(person1.married).toBe(false);
    expect(person2.married).toBe(false);

    divorce(person3, person4);
    expect(person3.married).toBe(false);
    expect(person4.married).toBe(false);
  })

  it(`removes the spouseName property entirely from both people`, () => {
    const person1 = {
      firstName: 'Colin',
      lastName: 'Jaffe',
      age: 39,
      married: true,
      spouseName: 'Petra Solano'
    };

    const person2 = {
      firstName: 'Petra',
      lastName: 'Solano',
      age: 29,
      married: true,
      spouseName: 'Colin Jaffe'
    };

    divorce(person1, person2)
    expect(person1.spouseName).toBe(undefined)
    expect(person2.spouseName).toBe(undefined)
    expect('spouseName' in person1).toBe(false)
    expect('spouseName' in person2).toBe(false)
  })
})

