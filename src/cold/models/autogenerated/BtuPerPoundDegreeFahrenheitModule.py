
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .NonSIUnitModule import NonSIUnit



from .EntropyPerMassUnitModule import EntropyPerMassUnit








class BtuPerPoundDegreeFahrenheit(DerivedUnit, NonSIUnit, EntropyPerMassUnit):
    """
    Class representing the `BtuPerPoundDegreeFahrenheit` entity, which inherits from:
    - DerivedUnit, NonSIUnit, EntropyPerMassUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#BtuPerPoundDegreeFahrenheit'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BtuPerPoundDegreeFahrenheit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BtuPerPoundDegreeFahrenheit(
    
    class_iri='https://w3id.org/emmo#BtuPerPoundDegreeFahrenheit',
    
    class_name='BtuPerPoundDegreeFahrenheit',
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#BtuPerPoundDegreeFahrenheit',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'BtuPerPoundDegreeFahrenheit',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    