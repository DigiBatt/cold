
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VectorModule import Vector



from .NumericalModule import Numerical



from .SpatialTileModule import SpatialTile



from .PrimaryDataModule import PrimaryData







class CycleNumberData(Vector, Numerical, SpatialTile, PrimaryData):
    """
    Class representing the `CycleNumberData` entity, which inherits from:
    - Vector, Numerical, SpatialTile, PrimaryData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ca48d41c_f5ea_4bf8_84ce_2d67fd9dad98'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CycleNumberData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CycleNumberData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ca48d41c_f5ea_4bf8_84ce_2d67fd9dad98',
    
    class_name='CycleNumberData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ca48d41c_f5ea_4bf8_84ce_2d67fd9dad98',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CycleNumberData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    