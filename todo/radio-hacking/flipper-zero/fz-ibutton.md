# FZ - iButton



## Intro

For more info about what is an iButton check:

{% content-ref url="../ibutton.md" %}
[ibutton.md](../ibutton.md)
{% endcontent-ref %}

## Design

The **blue** part of the following imageis how you would need to **put the real iButton** so the Flipper can **read it.** The **green** part is how you need to **touch the reader** with the Flipper zero to **correctly emulate an iButton**.

<figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

## Actions

### Read

In Read Mode Flipper is waiting for the iButton key to touch and is able to digest any of three types of keys: **Dallas, Cyfral, and Metakom**. Flipper will **figure out the type of the key itself**. The name of the key protocol will be displayed on the screen above the ID number.

### Add manually

It's possible to **add manually** an iButton of type: **Dallas, Cyfral, and Metakom**

### **Emulate**

It's possible to **emulate** saved iButtons (read or manually added).

{% hint style="info" %}
If you cannot make the expected contacts of the Flipper Zero touch the reader you can **use the external GPIO:**
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (24) (1).png" alt=""><figcaption></figcaption></figure>

## References

* [https://blog.flipperzero.one/taming-ibutton/](https://blog.flipperzero.one/taming-ibutton/)


