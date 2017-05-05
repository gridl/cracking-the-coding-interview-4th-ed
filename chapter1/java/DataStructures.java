import java.util.HashMap;
import 

public HashMap<Integer, Student> buildMap(Student[] students) {
        HashMap<Integer, student> map = new HashMap<Integer, Student>();
        for (Student s: students) {
            map.put(s.getId(), s);
        }
}

