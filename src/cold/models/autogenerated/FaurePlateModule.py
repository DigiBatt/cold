
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PastedPlateModule import PastedPlate







class FaurePlate(PastedPlate):
    """
    Class representing the `FaurePlate` entity, which inherits from:
    - PastedPlate

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_7aa76ea6_f388_4b1b_9d77_187526a1e31f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FaurePlate'`
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
    obj = FaurePlate(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_7aa76ea6_f388_4b1b_9d77_187526a1e31f',
    
    class_name='FaurePlate',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_7aa76ea6_f388_4b1b_9d77_187526a1e31f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FaurePlate',
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
    

    
    

    

    