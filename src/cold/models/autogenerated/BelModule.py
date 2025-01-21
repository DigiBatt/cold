
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SIAcceptedUnitModule import SIAcceptedUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .LogarithmicUnitModule import LogarithmicUnit








class Bel(SIAcceptedUnit, NonPrefixedUnit, LogarithmicUnit):
    """
    Class representing the `Bel` entity, which inherits from:
    - SIAcceptedUnit, NonPrefixedUnit, LogarithmicUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Bel'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Bel'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `uneceCommonCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `uneceCommonCode`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Bel(
    
    class_iri='https://w3id.org/emmo#Bel',
    
    class_name='Bel',
    
    hasSIConversionOffset="example_value",
    
    wikipediaReference="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    uneceCommonCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasSymbolValue="example_value",
    
    definition="example_value",
    
    dbpediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Bel',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Bel',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    uneceCommonCode: Optional[str] = Field(
        
            None,
        
        alias="uneceCommonCode"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasSymbolValue: Optional[str] = Field(
        
            None,
        
        alias="hasSymbolValue"
    )
    
    definition: Optional[str] = Field(
        
            None,
        
        alias="definition"
    )
    
    dbpediaReference: Optional[str] = Field(
        
            None,
        
        alias="dbpediaReference"
    )
    


    
    

    

    