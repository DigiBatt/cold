
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassModule import Mass



from .BatteryQuantityModule import BatteryQuantity







class ServiceMass(Mass, BatteryQuantity):
    """
    Class representing the `ServiceMass` entity, which inherits from:
    - Mass, BatteryQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_b10c88d8_43d9_42dd_9f65_49ce2314513f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ServiceMass'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ServiceMass(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_b10c88d8_43d9_42dd_9f65_49ce2314513f',
    
    class_name='ServiceMass',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_b10c88d8_43d9_42dd_9f65_49ce2314513f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ServiceMass',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    