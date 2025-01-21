
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .NonSIUnitModule import NonSIUnit



from .ThermalResistivityUnitModule import ThermalResistivityUnit



from .NonPrefixedUnitModule import NonPrefixedUnit








class DegreeFahrenheitHour(DerivedUnit, NonSIUnit, ThermalResistivityUnit, NonPrefixedUnit):
    """
    Class representing the `DegreeFahrenheitHour` entity, which inherits from:
    - DerivedUnit, NonSIUnit, ThermalResistivityUnit, NonPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#DegreeFahrenheitHour'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DegreeFahrenheitHour'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DegreeFahrenheitHour(
    
    class_iri='https://w3id.org/emmo#DegreeFahrenheitHour',
    
    class_name='DegreeFahrenheitHour',
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#DegreeFahrenheitHour',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'DegreeFahrenheitHour',
        
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    


    
    

    

    