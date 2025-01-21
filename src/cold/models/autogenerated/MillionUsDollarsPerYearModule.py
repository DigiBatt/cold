
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .NonSIUnitModule import NonSIUnit



from .FrequencyUnitModule import FrequencyUnit



from .NonPrefixedUnitModule import NonPrefixedUnit








class MillionUsDollarsPerYear(DerivedUnit, NonSIUnit, FrequencyUnit, NonPrefixedUnit):
    """
    Class representing the `MillionUsDollarsPerYear` entity, which inherits from:
    - DerivedUnit, NonSIUnit, FrequencyUnit, NonPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MillionUsDollarsPerYear'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MillionUsDollarsPerYear'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MillionUsDollarsPerYear(
    
    class_iri='https://w3id.org/emmo#MillionUsDollarsPerYear',
    
    class_name='MillionUsDollarsPerYear',
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MillionUsDollarsPerYear',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MillionUsDollarsPerYear',
        
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    


    
    

    

    