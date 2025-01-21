
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SISubMultiplePrefixModule import SISubMultiplePrefix







class Ronto(SISubMultiplePrefix):
    """
    Class representing the `Ronto` entity, which inherits from:
    - SISubMultiplePrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fbc2549b_9108_467a_a573_de48eb45cc4a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Ronto'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `hasNumericalValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNumericalValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Ronto(
    
    class_iri='https://w3id.org/emmo#EMMO_fbc2549b_9108_467a_a573_de48eb45cc4a',
    
    class_name='Ronto',
    
    hasSymbolValue="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fbc2549b_9108_467a_a573_de48eb45cc4a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Ronto',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    
    hasNumericalValue: Optional[str] = Field(
        None,
        alias="hasNumericalValue"
    )
    

    
    

    

    