    }
        hint_answer_edit_text = findViewById(R.id.hint_answer_edit_text);
        button9 = findViewById(R.id.button9);
        button9.setOnClickListener( new View.OnClickListener(){
            public void onClick(View v) {
                database = FirebaseDatabase.getInstance();
                reference = database.getReference("users");
                String idnum = editTextid_signup.getText().toString();
                String pass = editTextpass.getText().toString();
                String pass2 = editTextpass2.getText().toString();
                String qhint = editTextid_qhint.getText().toString();
                HelperClass helperClass = new HelperClass(idnum , pass , pass2 ,qhint);
                reference.child(idnum).setValue(helperClass);
                Toast.makeText(signup_page.this, "you have signup successfully!",Toast.LENGTH_LONG).show();
                Intent intent = new Intent(signup_page.this,done_page9.class);

            }
        });

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(signup_page.this,know_more_about_qhint.class));
            }
        });
