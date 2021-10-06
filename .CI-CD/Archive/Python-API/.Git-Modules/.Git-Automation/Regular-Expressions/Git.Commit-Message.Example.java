import java.util.regex.Matcher;
import java.util.regex.Pattern;

final String regex = "^.*?((\\[|\\])(Coverage|Code-Quality|Syntax|Best-Practices)(\\[|\\]))\\s*?(-|:|\\s\\s*?)?(\\[|\\])?\\W(.*$)";
final String string = "[Coverage] - 2 ' ' Hyphen Split\n\n"
	 + "[Code-Quality]: 1-Right ' ' Colon Split\n\n"
	 + "[Coverage] Single ' ' Split\n\n"
	 + "Project Build & [Coverage] Reporting\n\n"
	 + "[Syntax] : Reporting\n\n\n\n\n\n\n";
final String subst = "";

final Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE | Pattern.MULTILINE);
final Matcher matcher = pattern.matcher(string);

// The substituted value will be contained in the result variable
final String result = matcher.replaceAll(subst);

System.out.println("Substitution result: " + result);
