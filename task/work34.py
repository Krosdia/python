public class zuoye2 {
    public static void main(String[] args) {
          Student s1 = new Student();
                s1.setName("老邓");
                s1.setAge(18);
                s1.setGender("男");
                s1.setEnglish(100);
                s1.setMath(99);
                s1.setChinese(98);
                
                s1.study();
                s1.sum();
                s1.average();
    }
}
class Student {
    private String name;
    private int age;
    private String gender;
    private double english;
    private double math;
    private double chinese;
    
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public String getGender() {
        return gender;
    }
    public void setGender(String gender) {
        this.gender = gender;
    }
    public double getEnglish() {
        return english;
    }
    public void setEnglish(double english) {
        this.english = english;
    }
    public double getMath() {
        return math;
    }
    public void setMath(double math) {
        this.math = math;
    }
    public double getChinese() {
        return chinese;
    }
    public void setChinese(double chinese) {
        this.chinese = chinese;
    }
    
    
    public void study() {
        System.out.println("这位学生的姓名是:" + getName() + "\n\t" + "年龄:" + getAge() + "\n\t" + "性别:" + getGender() + "\n\t" + "英语成绩:" + getEnglish() + "\n\t" + "数学成绩:" + getMath() + "\n\t" + "语文成绩:" + getChinese() + "\n\t");
    }
    public void sum() {
        System.out.println("\t" + "总成绩:" + (getEnglish() + getMath() + getChinese()));
    }
    public void average() {
        System.out.println("\t" + "平均分:" + (getEnglish() + getMath() + getChinese())/3);
    }
    
}
 