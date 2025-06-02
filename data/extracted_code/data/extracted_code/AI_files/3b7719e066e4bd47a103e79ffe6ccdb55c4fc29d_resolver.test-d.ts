
import type { ArgValues, ExtractOptionValue, FilterArgs, ResolveArgValues } from './resolver.ts'

test('ExtractOptionValue', () => {
  // string type
  expectTypeOf<
    ExtractOptionValue<{
      type: 'string'
      short: 's'
    }>
  >().toEqualTypeOf<string>()

  // boolean type
  expectTypeOf<
    ExtractOptionValue<{
      type: 'boolean'
      short: 's'
    }>
  >().toEqualTypeOf<boolean>()

  // number type
  expectTypeOf<
    ExtractOptionValue<{
      type: 'number'
      short: 's'
    }>
  >().toEqualTypeOf<number>()

  // enum type
  expectTypeOf<
    ExtractOptionValue<{
      type: 'enum'
      short: 's'
      choices: ['a', 'b', 'c']
    }>
  >().toEqualTypeOf<'a' | 'b' | 'c'>()
  expectTypeOf<
    ExtractOptionValue<{
      type: 'enum'
      short: 's'
    }>
  >().toEqualTypeOf<never>()
})

test('FilterArgs', () => {
  expectTypeOf<
    FilterArgs<
      {
        help: {
          type: 'boolean'
          short: 'h'
        }
      },
      { help: true },
      'type'
    >
  >().toEqualTypeOf<{ help: true }>()
  expectTypeOf<
    FilterArgs<
      {
        help: {
          type: 'boolean'
          short: 'h'
        }
      },
      { help: true },
      'short'
    >
  >().toEqualTypeOf<{ help: true }>()

  expectTypeOf<
    FilterArgs<
      {
        help: {
          type: 'boolean'
          short: 'h'
        }
      },
      { help: true },
      'required'
    >
  >().toEqualTypeOf<{}>()
})

test('ResolveArgValues', () => {
  // basic
  expectTypeOf<
    ResolveArgValues<
      {
        help: {
          type: 'boolean'
          short: 'h'
        }
      },
      { help: true }
    >
  >().toEqualTypeOf<{ help?: true | undefined }>()

  // required
  expectTypeOf<
    ResolveArgValues<
      {
        help: {
          type: 'boolean'
          short: 'h'
          required: true
        }
      },
      { help: true }
    >
  >().toEqualTypeOf<{ help: true }>()

  // default
  expectTypeOf<
    ResolveArgValues<
      {
        help: {
          type: 'boolean'
          short: 'h'
          default: false
        }
      },
      { help: false }
    >
  >().toEqualTypeOf<{ help: false }>()

  // enum & choices
  expectTypeOf<
    ResolveArgValues<
      {
        log: {
          type: 'enum'
          short: 'l'
          choices: ['debug', 'info', 'warn', 'error']
        }
      },
      { log: 'debug' }
    >
  >().toEqualTypeOf<{ log?: 'debug' | undefined }>()
})