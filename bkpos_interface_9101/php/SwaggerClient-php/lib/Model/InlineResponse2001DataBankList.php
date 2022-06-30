<?php
/**
 * InlineResponse2001DataBankList
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Installment docs API
 *
 * <a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.35-SNAPSHOT
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * InlineResponse2001DataBankList Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class InlineResponse2001DataBankList implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'inline_response_200_1_Data_BankList';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'name_vi' => 'string',
'bank_short_name' => 'string',
'bank_code' => 'string',
'card_fee' => 'string',
'head_no_accept' => 'string[]',
'minimum_require' => 'string',
'loan_packages' => '\Swagger\Client\Model\InlineResponse2001DataLoanPackages[]'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'name_vi' => null,
'bank_short_name' => null,
'bank_code' => null,
'card_fee' => null,
'head_no_accept' => null,
'minimum_require' => null,
'loan_packages' => null    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'name_vi' => 'NameVi',
'bank_short_name' => 'BankShortName',
'bank_code' => 'BankCode',
'card_fee' => 'CardFee',
'head_no_accept' => 'HeadNoAccept',
'minimum_require' => 'MinimumRequire',
'loan_packages' => 'LoanPackages'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'name_vi' => 'setNameVi',
'bank_short_name' => 'setBankShortName',
'bank_code' => 'setBankCode',
'card_fee' => 'setCardFee',
'head_no_accept' => 'setHeadNoAccept',
'minimum_require' => 'setMinimumRequire',
'loan_packages' => 'setLoanPackages'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'name_vi' => 'getNameVi',
'bank_short_name' => 'getBankShortName',
'bank_code' => 'getBankCode',
'card_fee' => 'getCardFee',
'head_no_accept' => 'getHeadNoAccept',
'minimum_require' => 'getMinimumRequire',
'loan_packages' => 'getLoanPackages'    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['name_vi'] = isset($data['name_vi']) ? $data['name_vi'] : null;
        $this->container['bank_short_name'] = isset($data['bank_short_name']) ? $data['bank_short_name'] : null;
        $this->container['bank_code'] = isset($data['bank_code']) ? $data['bank_code'] : null;
        $this->container['card_fee'] = isset($data['card_fee']) ? $data['card_fee'] : null;
        $this->container['head_no_accept'] = isset($data['head_no_accept']) ? $data['head_no_accept'] : null;
        $this->container['minimum_require'] = isset($data['minimum_require']) ? $data['minimum_require'] : null;
        $this->container['loan_packages'] = isset($data['loan_packages']) ? $data['loan_packages'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets name_vi
     *
     * @return string
     */
    public function getNameVi()
    {
        return $this->container['name_vi'];
    }

    /**
     * Sets name_vi
     *
     * @param string $name_vi name_vi
     *
     * @return $this
     */
    public function setNameVi($name_vi)
    {
        $this->container['name_vi'] = $name_vi;

        return $this;
    }

    /**
     * Gets bank_short_name
     *
     * @return string
     */
    public function getBankShortName()
    {
        return $this->container['bank_short_name'];
    }

    /**
     * Sets bank_short_name
     *
     * @param string $bank_short_name bank_short_name
     *
     * @return $this
     */
    public function setBankShortName($bank_short_name)
    {
        $this->container['bank_short_name'] = $bank_short_name;

        return $this;
    }

    /**
     * Gets bank_code
     *
     * @return string
     */
    public function getBankCode()
    {
        return $this->container['bank_code'];
    }

    /**
     * Sets bank_code
     *
     * @param string $bank_code bank_code
     *
     * @return $this
     */
    public function setBankCode($bank_code)
    {
        $this->container['bank_code'] = $bank_code;

        return $this;
    }

    /**
     * Gets card_fee
     *
     * @return string
     */
    public function getCardFee()
    {
        return $this->container['card_fee'];
    }

    /**
     * Sets card_fee
     *
     * @param string $card_fee card_fee
     *
     * @return $this
     */
    public function setCardFee($card_fee)
    {
        $this->container['card_fee'] = $card_fee;

        return $this;
    }

    /**
     * Gets head_no_accept
     *
     * @return string[]
     */
    public function getHeadNoAccept()
    {
        return $this->container['head_no_accept'];
    }

    /**
     * Sets head_no_accept
     *
     * @param string[] $head_no_accept head_no_accept
     *
     * @return $this
     */
    public function setHeadNoAccept($head_no_accept)
    {
        $this->container['head_no_accept'] = $head_no_accept;

        return $this;
    }

    /**
     * Gets minimum_require
     *
     * @return string
     */
    public function getMinimumRequire()
    {
        return $this->container['minimum_require'];
    }

    /**
     * Sets minimum_require
     *
     * @param string $minimum_require minimum_require
     *
     * @return $this
     */
    public function setMinimumRequire($minimum_require)
    {
        $this->container['minimum_require'] = $minimum_require;

        return $this;
    }

    /**
     * Gets loan_packages
     *
     * @return \Swagger\Client\Model\InlineResponse2001DataLoanPackages[]
     */
    public function getLoanPackages()
    {
        return $this->container['loan_packages'];
    }

    /**
     * Sets loan_packages
     *
     * @param \Swagger\Client\Model\InlineResponse2001DataLoanPackages[] $loan_packages loan_packages
     *
     * @return $this
     */
    public function setLoanPackages($loan_packages)
    {
        $this->container['loan_packages'] = $loan_packages;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}