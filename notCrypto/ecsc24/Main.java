package ecsc24;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.spec.KeySpec;
import java.util.Base64;
import java.util.Map;
import java.util.UUID;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.Arrays;

import java.util.Objects;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String seed = reader.lines()
                .findFirst()
                .filter(line -> line.length() > 10)
                .orElse(UUID.randomUUID().toString());
        // String flag = Files.readString(Paths.get("flag.txt"));
        Encryptor encryptor = new Encryptor();
        // String ciphertext = encryptor.encrypt(flag, seed);
        // System.out.println(ciphertext);
        String flag = "GF7BaA0U0rzw3mEz1DNKA57Dbp2sP8fNsrm9t33scB5yOUOfpXTqSf75v1UsNt/47f0ueiBTlVA0Sn5OOauzSw==";
        String decrypt = encryptor.decrypt(flag, seed);
        System.out.println(decrypt);
    }
}

class Encryptor {
    private final Map<C, String> secrets = IntStream.range(Character.MIN_VALUE, Character.MAX_VALUE)
            .mapToObj(C::new)
            .collect(Collectors.toMap(
                    Function.identity(),
                    c -> UUID.randomUUID().toString()
            ));

    String generateRandomPassword(String userInput) {

        return userInput.chars()
                .mapToObj(i -> (char) i)
                .map(C::new)
                .map(secrets::get)
                .collect(Collectors.joining());
    }

    SecretKey getKeyFromPassword(String password) throws Exception {
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        KeySpec spec = new PBEKeySpec(password.toCharArray(), "Why so salty?".getBytes(), 65536, 256);
        return new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");
    }

    public String encrypt(String flag, String userInput) throws Exception {
        // 🥖
        System.out.println("flag: " + flag);
        System.out.println("userInput: " + userInput);
        String password = generateRandomPassword(userInput);
        System.out.println("password: " + password);
        
        SecretKey key = getKeyFromPassword(generateRandomPassword(userInput));

        // 🥖
        byte[] encoded = ((SecretKeySpec)key).getEncoded();
        System.out.println(Base64.getEncoder().encodeToString(encoded));

        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] cipherText = cipher.doFinal(flag.getBytes());
        return Base64.getEncoder().encodeToString(cipherText);
    }

    // 🥖
    public String decrypt(String flag, String userInput) throws Exception {
        System.out.println("flag: " + flag);
        System.out.println("userInput: " + userInput);
        String password = generateRandomPassword(userInput);
        System.out.println("password: " + password);
        
        SecretKey key = getKeyFromPassword(generateRandomPassword(userInput));

        byte[] decodedFlag = Base64.getDecoder().decode(flag);

        byte[] encoded = ((SecretKeySpec)key).getEncoded();
        System.out.println(Base64.getEncoder().encodeToString(encoded));

        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] clearText = cipher.doFinal(decodedFlag);
        return Base64.getEncoder().encodeToString(clearText);
    }
}


class C {
    private final Integer index;

    public C(Integer index) {
        this.index = index;
    }

    public C(Character c) {
        this.index = (int) c;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        C a = (C) o;
        return index == a.index;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(index);
    }
}
