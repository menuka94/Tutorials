package org.test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.github.jknack.handlebars.Handlebars;
import com.github.jknack.handlebars.Template;

public class Main {
    private static final String PARAM_MAP = "param-map";
    private static final String CUSTOM_OBJECT = "custom-object";
    private static final String TEMPLATE = "template";

    public static void main(String[] args) throws IOException {
        processTemplate(TEMPLATE);
    }

    public static void processTemplate(String method) throws IOException {
        Handlebars handlebars = new Handlebars();
        Template template = handlebars.compileInline("Hi {{name}}!");
        String templateString = "";

        switch (method) {
            case PARAM_MAP:
                Map<String, String> parameterMap = new HashMap<>();
                parameterMap.put("name", "John");
                templateString = template.apply(parameterMap);
                break;
            case CUSTOM_OBJECT:
                Person person1 = new Person();
                person1.setName("John");
                templateString = template.apply(person1);
                break;
            case TEMPLATE:
                template = handlebars.compile("greeting");
                Person person2 = new Person();
                person2.setName("John");
                person2.getAddress().setStreet("York Street");
                person2.addFriend(new Person("Sarah"));
                person2.addFriend(new Person("Louis"));
                person2.setBusy(true);

                templateString = template.apply(person2);
                break;
            default:
                System.out.println("Error");
        }

        System.out.println(templateString);

    }

    public static class Person {
        private String name;
        private boolean busy;
        private List<Person> friends = new ArrayList<>();
        private Address address;

        public Person() {
            address = new Address();
        }

        public Person(String name) {
            this();
            this.name = name;
        }

        public boolean isBusy() {
            return busy;
        }

        public void setBusy(boolean busy) {
            this.busy = busy;
        }

        public List<Person> getFriends() {
            return friends;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void addFriend(Person friend) {
            friends.add(friend);
        }

        public Address getAddress() {
            return address;
        }

        public static class Address {
            private String street;

            public String getStreet() {
                return street;
            }

            public void setStreet(String street) {
                this.street = street;
            }
        }
    }
}
