  {
    'targets': [
      {
        'target_name': 'sqlite3',
        'type': '<(library)',
        
        'dependencies': [
        ],

        'defines': [
        ],
        
        'include_dirs': [
          '.',
        ],

        'sources': [
          'sqlite3.c',          
        ],

        'conditions': [
          ['OS=="ios"', {
            'include_dirs': [
            ],

            'sources': [
            ],

            'defines': [              
            ],
          }],
          
          ['OS=="android"', {
            'defines': [              
            ]
          }],

          ['OS=="linux"', {
          }],
          
          ['OS=="winphone"', {
          }],

          ['OS=="win32"', {
          }]
        ],
      },
    ],
  }