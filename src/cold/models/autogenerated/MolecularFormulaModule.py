
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalFormulaModule import ChemicalFormula





from .SpatialTileModule import SpatialTile





class MolecularFormula(ChemicalFormula):
    """
    Class representing the `MolecularFormula` entity, which inherits from:
    - ChemicalFormula

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4208f937_8bad_47cf_af46_4ada75e63adb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MolecularFormula'`
        - **Alias**: `class_name`
    
    - `hasSpatialTile` (`Optional[SpatialTile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialTile`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MolecularFormula(
    
    class_iri='https://w3id.org/emmo#EMMO_4208f937_8bad_47cf_af46_4ada75e63adb',
    
    class_name='MolecularFormula',
    
    hasSpatialTile="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4208f937_8bad_47cf_af46_4ada75e63adb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MolecularFormula',
        alias="class_name"
    )
    
    hasSpatialTile: Optional[SpatialTile] = Field(
        None,
        alias="hasSpatialTile"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    @validator("hasSpatialTile", pre=True, always=True)
    def validate_hasSpatialTile(cls, value):
        if value is not None and not isinstance(value, SpatialTile):
            raise ValueError(f"Field 'hasSpatialTile' must be an instance of 'SpatialTile' or its subclass.")
        return value
    
    

    

    