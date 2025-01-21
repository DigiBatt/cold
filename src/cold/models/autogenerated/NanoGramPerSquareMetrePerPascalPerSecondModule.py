
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel








class NanoGramPerSquareMetrePerPascalPerSecond(LinkedDataModel):
    """
    Class representing the `NanoGramPerSquareMetrePerPascalPerSecond` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#NanoGramPerSquareMetrePerPascalPerSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NanoGramPerSquareMetrePerPascalPerSecond'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NanoGramPerSquareMetrePerPascalPerSecond(
    
    class_iri='https://w3id.org/emmo#NanoGramPerSquareMetrePerPascalPerSecond',
    
    class_name='NanoGramPerSquareMetrePerPascalPerSecond',
    
    qudtReference="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    wikipediaReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#NanoGramPerSquareMetrePerPascalPerSecond',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'NanoGramPerSquareMetrePerPascalPerSecond',
        
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    


    
    

    

    